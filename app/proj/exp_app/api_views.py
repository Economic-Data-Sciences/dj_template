from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.response import Response
from rest_framework.views import APIView

from django.http import StreamingHttpResponse

from .models import StreamingVariable, StateMetrics
from .serializers import StreamingVariableSerializer, StateMetricsSerializer
import random
import logging
import time
from decimal import Decimal
from django.db import connection


logger = logging.getLogger(__name__)

# an example api view
@api_view(['GET'])
def example(request):
    return Response("Hello World", status=HTTP_200_OK)

# get current state
@api_view(['GET'])
def get_latest(request):
    # user streaming variable object to get most recent state
    latest = StreamingVariable.objects.latest('id')
    latest_s = StreamingVariableSerializer(latest)
    return Response(latest_s.data, status=HTTP_200_OK)

# get state metrics
@api_view(['GET'])
def get_metrics(request):
    """
    Get the average values for each state.
    """
    # get the average values
    def get_metrics_sql():
        with connection.cursor() as cursor:
            cursor.execute("SELECT state, AVG(value) as avg_value, STDDEV(value) as sd_value FROM streaming_variable GROUP BY state")
            rows = cursor.fetchall()

        return rows
    
    # create list
    metrics = get_metrics_sql()
    metrics_list = []
    for metric in metrics:
        metric_obj = StateMetrics(
            state = metric[0],
            avg_value = metric[1],
            sd_value = metric[2]
        )
        metrics_list.append(metric_obj)
    # serialize and return
    metrics_s = StateMetricsSerializer(metrics_list, many=True)
    return Response(metrics_s.data, status=HTTP_200_OK)

# stream random data
class StreamGeneratorView(APIView):
    """
    A view that streams random data.
    """
    def __init__(self):
        super(StreamGeneratorView, self).__init__()
        logger.info('StreamGeneratorView init')
        self.state = 'POS'
        self.all_states = ['POS', 'NEG', 'VOL']

    def update_state(self):
        rnd1 = random.randint(0, 100)
        logger.info('rnd1: {}'.format(rnd1))
        if rnd1 < 66:
            logger.info('keeping state')
            return self.state
        else:
            # list of remaining states
            logger.info('changing state')
            # remove current state from list
            avail_states = [x for x in self.all_states if x != self.state]
            rnd2 = random.randint(0, 100)
            if rnd2 < 50:
                new_state = avail_states[0]
            else:
                new_state = avail_states[1]
            self.state = new_state
            return self.state
        
    def gen_state_data(self):
        if self.state == 'POS':
            d = Decimal(random.random() - 0.3)
        elif self.state == 'NEG':
            d = Decimal(random.random() - 0.7)
        elif self.state == 'VOL':
            d = Decimal((random.random() - 0.5) * 2.0)
        else:
            d = Decimal(0.0)
        return d
        

    def gen_random_data(self):
        while True:
            time.sleep(0.5)
            self.update_state()
            d = self.gen_state_data()
            data_obj = StreamingVariable(
                name = 'demo state variable',
                state = self.state,
                value = d
            )
            data_obj.save()
            data_s = StreamingVariableSerializer(data_obj)
            yield data_s.data

    def get(self,request):
        data_s = self.gen_random_data()
        response =  StreamingHttpResponse(data_s, status=HTTP_200_OK, content_type='text/event-stream')
        response['Cache-Control']= 'no-cache',
        return response



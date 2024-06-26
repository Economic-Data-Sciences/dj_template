from django.db import models

# Create your models here.

class StreamingVariable(models.Model):
    """
    Model for storing streaming variables
    """
    # adding state variables
    class StateVariable(models.TextChoices):
        NEGATIVE = 'NEG', ('Negative')
        POSITIVE = 'POS', ('Positive')
        VOLATILE = 'VOL', ('Volatile')  
    name = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    state = models.CharField(max_length=3, choices=StateVariable.choices, default=StateVariable.POSITIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Streaming Variable'
        verbose_name_plural = 'Streaming Variables'
        db_table = 'streaming_variable'

    def __str__(self):
        return "{} - {}: {}".format(self.name, self.state, self.created_at)
    

class StateMetrics(models.Model):
    """
    Model for storing State averages
    """
    state = models.CharField(max_length=3, primary_key=True)
    avg_value = models.DecimalField(max_digits=10, decimal_places=2)
    sd_value = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ['state']
        managed = False


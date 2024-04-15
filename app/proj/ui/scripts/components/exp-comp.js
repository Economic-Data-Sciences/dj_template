import React, { Component } from 'react';
import axios from 'axios';

export default class Example extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: []
    };
  }

  componentDidMount() {
    axios.get('/api/example')
      .then(res => {
        console.log(res.data);
        const data = res.data;
        this.setState({ data });
      })
      .catch(console.log);
  }

  render() {
    return (
      <div>
        <h1>{this.state.data} Example</h1>
        <p>This is an example component.</p>
      </div>
    );
  }
}
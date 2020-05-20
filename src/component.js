import React from 'react';

class Car extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      brand: "Ford",
      model: "Mustang",
      color: "red",
      year: 1964
    };
  }
  render() {
    return (
      <div>
        <h1>My {this.state.brand}</h1>
        <p>
          It is a {this.state.color}
          {this.state.model}
          from {this.state.year}.
        </p>
      </div>
    );
  }
}





class Device extends React.Component{
    constructor(props) {
        super(props);
        this.state = {
            owner: props.owner,
            state: props.state,
            deleted_at: props.deleted_at,
            url: props.url,
        };
    }
}

class Bulb extends Device{
    constructor(props) {
        super(props);
        this.state = {
            brightness: props.brightness,
            color: props.color,
        }
    }
}



class Fan extends Device{
    constructor(props) {
        super(props);
        this.state = {
            speed: props.speed,
        }
    }

}

export {Car};
export {Bulb};
export {Fan}
import React, { Component } from 'react'
import Table from './Table'
import Form from './Form';
import axios from 'axios';

class App extends Component {
  state = {
        characters: []
    }

    removeCharacter = index => {
      const { characters } = this.state
      let character = characters[index];

      if (this.makeDeleteCall(character)) {
        this.setState({
          characters: characters.filter((character, i) => {
            return i !== index;
          }),
        });
      }
    };

    makeDeleteCall(character) {
      return axios
        .delete("http://localhost:5000/users", { 
          data : {id:character.id,job:character.job,name:character.name} , 
          headers: {"Authorization": "***"}} )
        .then(function (response) {
          console.log(response);
          return true;
        })
        .catch(function (error) {
          console.log(error);
          return false;
        });
    }

    handleSubmit = character => {
      this.makePostCall(character).then( callResult => {
         if (/*callResult ===*/ true) {
           console.log(character);
           this.setState({ characters: [...this.state.characters, callResult] });
         }
      });
    }

    componentDidMount() {
      axios.get('http://localhost:5000/users')
       .then(res => {
         const characters = res.data.users_list;
         this.setState({ characters });
       })
       .catch(function (error) {
         //Not handling the error. Just logging into the console.
         console.log(error);
       });
    }

    makePostCall(character){
      return axios.post('http://localhost:5000/users', character)
       .then(function (response) {
         console.log(response);
         character = response.data;
         return character;
       })
       .catch(function (error) {
         console.log(error);
         return false;
       });
    }

    render() {
      const { characters } = this.state
    
      return (
        <div className="container">
          <Table characterData={characters} removeCharacter={this.removeCharacter} />
          <Form handleSubmit={this.handleSubmit}/>
        </div>
      )
    }
  }

export default App
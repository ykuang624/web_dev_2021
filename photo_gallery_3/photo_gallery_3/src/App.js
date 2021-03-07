import logo from './logo.svg';
import './App.css';
import React from 'react';

const BASE_URL = "https://api.unsplash.com/"
class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      value:0, 
      photos:[]
    };

    this.handleChange = this.handleChange.bind(this);
  };



  handleUpdate=(e)=>{
    e.preventDefault();
    if(this.state.value != 0){
      const url = BASE_URL+"photos/random/"+`?count=${this.state.value}&client_id=3n1HctiZHJGD6yWl88T7u9DaznFeKTbemn70KYo4lYU`;
      fetch(url).then((httpResponse)=>httpResponse.json()).then((data)=>this.updatePhotoData(data));
    }else{
      alert("Please enter a number between 1 and 4")
    }
  };

  updatePhotoData(data){
    const photosNew = data.map((item)=>{
      return{photoUrl: item.urls.raw}
    })
    this.setState({photos:photosNew})
  }

  handleChange(e){
    this.setState({value:e.target.value})
  };
  render = () => {
    const galleryWall = this.state.photos.map(function(item){
      return(
        <section className = "col-md-6 my-5 photo">
          <img className="img-fluid rounded" src = {item.photoUrl}></img>
        </section>
      )
    })
  
    return(
      <div className="container w-100 h-100 ml-0 mr-0">
        <div className="row h-100">
          <div className="col-md-3 bg-dark text-white m-0 d-flex align-items-center">
            <section className="text-center m-auto">
              <h1>Photo Gallery</h1>
              <text className="font-italic">photos from unsplash.com</text>
              <p className="font-italic text-muted">Yue Kuang 2021</p>
              <br></br>
              <form>
              <label for="photo_num">Number of Photos to Display</label>
                <br></br>
                <input type="number" id="photo_num" max="4" min="1" value={this.state.value} onChange={this.handleChange} />
                <button onClick={this.handleUpdate} className="btn btn-secondary ml-3">Update</button>
              </form>
              <br></br>
            </section>
          </div>
          <div className="col-md-9 m-0 d-flex align-items-center">
            <div className="container w-100 h-100 m-0 ">
              <div className="row h-100">
                {galleryWall}
              </div>
            </div>
          </div>

        </div>
      </div>
    )

  }
}

export default App;

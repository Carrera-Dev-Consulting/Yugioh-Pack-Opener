import { Routes, Route } from "react-router-dom";
import logo from './assets/logo.svg';
import './App.css';
import { DefinedServices } from './bootstrap';
import { Home } from './views/home';
import { Yugioh } from "./views/yugioh";

type AppProps = {
  services: DefinedServices
}


function App(props: AppProps) {
  // TODO: Build out to load all views and add the header with navbar and footer
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <h1>Yugioh Card Puller</h1>
      </header>
      {/* <section>
        <Home services={props.services} />
      </section> */}
      <Routes>
        <Route path="/" element={ <Home services={props.services} /> } />
        <Route path="yugioh" element={ <Yugioh services={props.services} /> } />
      </Routes>
    </div>
  );
}

export default App;

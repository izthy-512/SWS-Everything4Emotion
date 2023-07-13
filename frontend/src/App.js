import React, { useEffect } from "react";
import { Router } from "@reach/router";

import NavBar from "./components/NavBar";
import InputPage from './pages/InputPage';
import Feed from "./pages/Feed";
import NotFound from "./pages/NotFound";

import './App.css';
import "./utilities.css"

const App = () => {

  useEffect(() => { }, []);

  return (
    <>
      <NavBar />
      <div className="App">
        <Router>
          <InputPage path="/" />
          <Feed path="/feed/" />
          <NotFound default />
        </Router>
      </div>
    </>
  );
}

export default App;

import "./styles.css";

var data = require ("./MOCK_DATA.json");

export default function App() {
    return(
        <div className="App">
        <h1>Search</h1>

        <div className= "search-container">
        <div className="search-inner"></div>
        </div>
        </div>
    );
}
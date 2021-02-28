'use strict';
const csrftoken = Cookies.get('csrftoken');

const App = ()=> {
    return(
        <div>
            <h3>Hello, world!</h3>
        </div>
    )
}

ReactDOM.render(<App/>, document.getElementById('root'));
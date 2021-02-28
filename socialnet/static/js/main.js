'use strict';

const csrftoken = Cookies.get('csrftoken');

const get_posts = async () => {
    let posts = await fetch("/api/posts/")
        .then(res => res.json())
        .then(posts_list => {
            return posts_list
        });
    await console.log(posts);
    return posts;
};

const App = ()=> {
    const [posts, setPosts] = React.useState([]);
    const [refresh, setRefresh] = React.useState(false);

    React.useEffect(()=>{
        let all_posts = get_posts();
        all_posts.then(data => setPosts(data));
    }, [refresh]);

    return(
        <div>
            <h3>Hello, world!</h3>
            {posts.map((item, ind)=>{
                return <div key={ind+10}>
                    <h4>{item.title}</h4>
                    <p>{item.content}</p>
                    <a href={item.url}>Details</a>
                </div>
            })}
        </div>
    )
}

ReactDOM.render(<App/>, document.getElementById('root'));
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

const post_rud = async (postId, method='GET', data={}) => {
    await fetch(`/api/posts/${postId}/`, {
        method: method,
        headers: {
            'Content-Type': 'application/json;charset=utf-8',
            "X-CSRFToken": csrftoken,
        },
        body: method === 'GET' ? null : JSON.stringify(data),
    })
        .then(res => res.json())
        .then(obj => obj);
};

const post_create = async ( data={}) => {
    await fetch(`/api/posts/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json;charset=utf-8',
            "X-CSRFToken": csrftoken,
        },
        body: JSON.stringify(data),
    })
        .then(res => res.json())
        .then(obj => obj);
};

const App = ()=> {
    const [posts, setPosts] = React.useState([]);
    const [refresh, setRefresh] = React.useState(false);

    React.useEffect(() => {
        let all_posts = get_posts();
        all_posts.then(data => setPosts(data));
    }, [refresh]);

    return(
        <div className="col col-lg-8">
            {posts.map((item, ind)=>{
                return (
                    <div key={ind + 10}>
                        <div className="card mt-5">
                            <img src={item.image_cover || "https://loremflickr.com/150/100"} className="card-img-top" alt=""/>
                            <div className="card-body">
                                <h5 className="card-title">{item.title}</h5>
                                <p className="card-text">{item.content}.</p>
                                <div className="row gx-1 mb-3">
                                    <div className="col p-1 border bg-light"><strong>Date:</strong> {new Date(item.created).toLocaleDateString()}</div>
                                    <div className="col p-1 border bg-light"><strong>Likes:</strong> {item.likes}</div>
                                    <div className="col p-1 border bg-light"><strong>Author:</strong> {item.user.email}</div>
                                </div>
                                <div className="row gx-1">
                                    <a href={item.url} className="d-block col btn btn-primary">Go to API</a>
                                    <button className="d-block col btn btn-secondary"
                                            onClick={()=>{
                                                post_rud(item.id, 'PATCH', {"likes": item.likes+1});
                                                setRefresh(!refresh);
                                            }}>Like</button>
                                    <button className="d-block col btn btn-danger"
                                            onClick={()=>{post_rud(item.id, 'DELETE'); setRefresh(!refresh)}}>Delete</button>
                                </div>
                            </div>
                        </div>
                    </div>
                )
            })}
        </div>
    )
}

ReactDOM.render(<App/>, document.getElementById('root'));
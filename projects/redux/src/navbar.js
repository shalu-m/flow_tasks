function Navbar(props){
    return(
        <>
        <nav class="navbar navbar-light bg-light justify-content-between">
            <a class="navbar-brand">Navbar</a>

            <h3>Welcome {props.username}</h3>
            <form class="form-inline">
            
    
            {props.login?<button onClick={()=>props.login(false)}>log out</button>:<button>log in</button>}
            </form>
        </nav>
        </>
    )
}
export default Navbar;
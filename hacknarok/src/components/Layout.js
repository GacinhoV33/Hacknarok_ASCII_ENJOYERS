import MainMenu from "./MainMenu";
import classes from "./Layout.module.css";

function Layout(props){
    return (
        <div>
            <MainMenu />
            <main className={classes.main}>{props.children}</main>
        </div>
    );
}

export default Layout;
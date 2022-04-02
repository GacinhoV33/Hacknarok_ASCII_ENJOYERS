import classes from "./SubDetail.module.css";

function Backdrop(props)
{
    function cancelHandler(e){
        e.stopPropagation();
        props.onCancel();
    }
    return <div className={classes.backdrop} onClick={cancelHandler}/>;
}

export default Backdrop;
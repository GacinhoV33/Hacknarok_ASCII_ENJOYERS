import classes from "./SubDetail.module.css";
import classes2 from "./SubSimple.module.css";

function SubDetail(props){

    function cancelHandler(e){
        e.stopPropagation();
        props.onCancel();
    }

    function deleteHandler(e){
        e.stopPropagation();
        props.onDelete();
    }

    return (
        <div className={classes.modal}>
            <div className={classes.row}>
                <div className={classes2.comp_name}><p>{props.company}</p></div>
                <div className={classes2.amount}><p>Opłata: {props.amount} złotych</p></div>
                <div className={classes2.period}><p>Okres rozliczeniowy: {props.period} miesięcy</p></div>
            </div>
            <div className={classes.row}>
                <div>
                    <a href={props.link} target="_blank">
                        <div className={classes.service_page}><p>Strona serwisu</p></div>
                    </a>
                </div>
                <div>
                    <button className={classes.btn_red} onClick={deleteHandler}>Usuń</button>
                </div>
                <div>
                    <button className={classes.btn} onClick={cancelHandler}>Zamknij</button>
                </div>
            </div>
            
        </div>);
}
export default SubDetail;
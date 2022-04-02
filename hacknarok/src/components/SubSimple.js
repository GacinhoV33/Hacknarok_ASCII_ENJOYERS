import classes from "./SubSimple.module.css";
import {useState} from 'react';
import SubDetail from "./SubDetail";
import Backdrop from "./Backdrop";

function SubSimple(props){
    const [modalIsOpen, setModalIsOpen] = useState(false);

    function detailHandler(){
        setModalIsOpen(true);
    }

    function closeModal(){
        setModalIsOpen(false);
    }

    return (
        <section className={classes.sub} onClick={detailHandler}>
            <div className={classes.comp_name}><p>{props.company}</p></div>
            <div className={classes.amount}><p>Opłata: {props.amount} złotych</p></div>
            <div className={classes.period}><p>Okres rozliczeniowy: {props.period} miesięcy</p></div>
            { modalIsOpen ? <SubDetail onCancel={closeModal} onDelete={closeModal} company={props.company} amount={props.amount} period={props.period} link={props.link}/> : null}           
            { modalIsOpen ? <Backdrop onCancel={closeModal}/> : null}      
        </section>
    );
}

export default SubSimple;

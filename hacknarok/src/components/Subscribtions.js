import SubSimple from "./SubSimple";
import classes from "./Subscribtions.module.css";
import {useState, useEffect} from 'react';
import NewSubForm from "./NewSubForm";
import Backdrop from "./Backdrop";

const DUMMY_DATA = 
[
    {id: 1, company: "Netflix", amount: 20, period: 1, link: "https://www.netflix.com"},
    {id: 2, company: "Amazon Prime", amount: 30, period: 1, link: "https://www.primevideo.com/"},
    {id: 3, company: "Spotify", amount: 200, period: 3, link: "https://www.spotify.com"}
];

const AVAILABLE_SUBSCIRBTIONS = [
    {name:"Netflix",
    plans:["plan1", "plan2"]},

    {name:"Spotify",
    plans:["plan1", "plan3", "plan4"]},
]

function Subscribtions(){
    const [formIsOpen, setFormIsOpen] = useState(false);
    const [isLoading, setIsLoading] = useState(true);
    const [loadedSubscribtions, setLoadedSubscribtions] = useState([]);

    function openFormHandler(){
        setFormIsOpen(true);
    }

    function closeFormHandler(){
        setFormIsOpen(false);
    }

    useEffect(() => {
            setIsLoading(true);
            fetch("dupa123").then((response) => {
                return response.json();
              }).then((data) => {
                    setLoadedSubscribtions(data.lista);
                    setIsLoading(false);
                }
            )
        });

    if (isLoading) {
        return (
            <div className={classes.page_wrapper}>
                <div className={classes.row}>
                    <div className={classes.row_add}>
                        <div className={classes.add_sub} onClick={openFormHandler}><p>Dodaj subskrybcję</p></div>
                        { formIsOpen ? <NewSubForm onCancel={closeFormHandler} subs={AVAILABLE_SUBSCIRBTIONS}/> : null} 
                        { formIsOpen ? <Backdrop onCancel={closeFormHandler}/> : null} 
                    </div>
                </div>
                <div className={classes.row}>
                    <section>
                        <p>Loading...</p>
                    </section>
                </div>
            </div>
            
        );
    }
    else{
        return (
            <div className={classes.page_wrapper}>
                <div className={classes.row}>
                    <div className={classes.row_add}>
                        <div className={classes.add_sub} onClick={openFormHandler}><p>Dodaj subskrybcję</p></div>
                        { formIsOpen ? <NewSubForm onCancel={closeFormHandler} subs={AVAILABLE_SUBSCIRBTIONS}/> : null} 
                        { formIsOpen ? <Backdrop onCancel={closeFormHandler}/> : null} 
                    </div>
                </div>
                <div className={classes.row}>
                    <div className={classes.subs_wrapper}>
                        {loadedSubscribtions.map((sub) => (<SubSimple key={sub.id} company={sub.company} amount={sub.amount} period={sub.period} link={sub.link}/>))}
                    </div>
                </div>
            </div>
        );
    }
}

export default Subscribtions;
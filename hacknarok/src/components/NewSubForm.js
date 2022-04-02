import classes from "./NewSubForm.module.css";
import classes_modal from "./SubDetail.module.css";
import { useRef } from 'react';
import Select from "react-select";

function NewSubForm(props){
    const nameInputRef = useRef();
    const priceInputRef = useRef();
    const startDateInputRef = useRef();
    const planInputRef = useRef();

    function submitHandler(event) {
    event.preventDefault();

    const enteredName = nameInputRef.current.value;
    const enteredPrice = priceInputRef.current.value;
    const enteredStartDate = startDateInputRef.current.value;
    const enteredPlan = planInputRef.current.value;

    const meetupData = {
        name: enteredName,
        price: enteredPrice,
        plan: enteredStartDate,
        startDate: enteredPlan,
        };
    }

    let options = [];
    let options2 = [];
    props.subs.forEach((el) => {options.push({value:el.name, label:el.name})})

    function changeSelect(e){
        options2 = [];
        const record = props.subs.filter(sub => sub.name==e.value)
        record[0].plans.forEach(el => options2.push({value:el, label:el}))
        console.log(options2)
    }

    return(
        <div className={classes_modal.modal}>
            <Select options={options} onChange={changeSelect}/>
            <Select options={options2} />
        </div>
    );
}

export default NewSubForm;

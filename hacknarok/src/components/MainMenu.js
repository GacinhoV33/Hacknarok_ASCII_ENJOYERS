import classes from './MainMenu.module.css';
import { Link } from 'react-router-dom';

function MainMenu(){
    return (
        <header className={classes.header}>
            <div className={classes.central}>
                <div className={classes.logo}>
                    Manager subskrybcji
                </div>
                <nav>
                    <Link to="/"><div className={classes.menu_link}><p>Twoje subskrybcje</p></div></Link>
                    <Link to="/analysys"><div className={classes.menu_link}><p>Analizy</p></div></Link>
                </nav>
            </div>
        </header>
    );
}

export default MainMenu;
import { Route, Routes } from 'react-router-dom';
import Subscribtions from './components/Subscribtions';
import Analysis from './components/Analysis';
import Layout from './components/Layout';

function App() {
  return (
    <Layout>
      <Routes>
        <Route path="/" element={<Subscribtions />}/>
        <Route path="/analysys" element={<Analysis />}/>
      </Routes>
    </Layout>
  );
}

export default App;

import React, {useEffect, useState} from 'react';
import EmailList from './components/EmailList';
import EmailDetail from './components/EmailDetail';
import './styles.css';

function App(){
  const [emails, setEmails] = useState([]);
  const [selected, setSelected] = useState(null);

  useEffect(()=>{
    fetch('http://localhost:8000/emails')
      .then(r=>r.json())
      .then(setEmails)
      .catch(err=> console.error(err));
  },[]);

  return (
    <div className="container">
      <div className="sidebar">
        <h2>Prioritized Emails</h2>
        <EmailList emails={emails} onSelect={setSelected} />
      </div>
      <div className="main">
        <EmailDetail email={selected} onUpdate={(updated)=>{
            setEmails(emails.map(e=> e.id===updated.id?updated:e))
        }} />
      </div>
    </div>
  )
}
export default App;

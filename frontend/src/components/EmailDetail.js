import React, {useState, useEffect} from 'react';

export default function EmailDetail({email,onUpdate}){
  const [reply, setReply] = useState('');
  useEffect(()=>{ setReply('') }, [email]);
  if(!email) return <div className="placeholder">Select an email</div>
  return (
    <div>
      <h3>{email.subject}</h3>
      <div><b>From:</b> {email.sender}</div>
      <div className="body">{email.body}</div>
      <div className="extracted"><b>Extracted:</b> {JSON.stringify(email.extracted)}</div>
      <div style={{marginTop:10}}>
        <button onClick={async ()=>{
          const res = await fetch(`http://localhost:8000/email/${email.id}/generate-reply`,{method:'POST'})
          const data = await res.json()
          setReply(data.body)
          const updated = {...email, suggested_reply: data.body}
          onUpdate(updated)
        }}>Generate Reply</button>
      </div>
      <div style={{marginTop:10}}>
        <textarea value={reply || email.suggested_reply || ''} onChange={e=>setReply(e.target.value)} rows={8} style={{width:'100%'}} />
      </div>
      <div style={{marginTop:10}}>
        <button onClick={async ()=>{
          await fetch(`http://localhost:8000/email/${email.id}/send`,{
            method:'POST',
            headers:{'Content-Type':'application/json'},
            body: JSON.stringify({review_text: reply})
          })
          alert('Marked as resolved (demo)')
        }}>Send / Mark Resolved</button>
      </div>
    </div>
  )
}

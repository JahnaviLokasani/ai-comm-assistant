import React from 'react';
export default function EmailList({emails,onSelect}){
  return (
    <div>
      {emails.map(e=> (
        <div key={e.id} onClick={()=>onSelect(e)} className="email-item">
          <div className="email-subject">{e.subject}</div>
          <div className="email-meta">{e.sender} • {e.priority} • {e.sentiment}</div>
        </div>
      ))}
    </div>
  )
}

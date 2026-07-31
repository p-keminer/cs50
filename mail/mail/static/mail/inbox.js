console.log("inbox.js geladen");
document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);

  document.querySelector('#compose-form').addEventListener('submit', send_email);
  

  // By default, load the inbox
  load_mailbox('inbox');
});

function compose_email() {

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';
  document.querySelector('#email-view').style.display = 'none';

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';

}

function compose_email_filled(email, mailbox){

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';
  document.querySelector('#email-view').style.display = 'none';

  // Clear out composition fields
  if(mailbox === "sent"){
     document.querySelector('#compose-recipients').value = email.recipients;
  } else {
  document.querySelector('#compose-recipients').value = email.sender;
  }

  if(email.subject.startsWith('Re')) {
    document.querySelector('#compose-subject').value = email.subject;
  } else {
    document.querySelector('#compose-subject').value = 'Re: ' + email.subject;
  }
  document.querySelector('#compose-body').value ='\n\n\n\n' + 'On ' + email.timestamp + ' ' + email.sender + ' wrote: ' + '\n\n' + email.body ;

}

function load_mailbox(mailbox) {
  
  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';
  
  document.querySelector('#email-view').style.display = 'none';
  document.querySelector('#email-view').innerHTML = '';

  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;
  
  //console.log(event)
  show_mailbox(mailbox);

}

function toggle_read(email_id, bool) {

  fetch(`/emails/${email_id}`, {
    method: 'PUT',
    body: JSON.stringify({
        read: bool
    })
  });

}

function toggle_archived(email_id, bool) {

  return fetch(`/emails/${email_id}`, {
    method: 'PUT',
    body: JSON.stringify({
        archived: bool
    })
  });

}

function show_email(mailbox, email_id ) {

  // views umschalten
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#email-view').style.display = 'block';

  //titel anzeigen
  document.querySelector('#email-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;

  // email auf gelesen setzen
  toggle_read(email_id, true)

  // email holen
  fetch(`/emails/${email_id}`)
  .then(response => response.json())
  .then(email => {
    
    //console.log(email);
    
    // email erstellen
    const div = document.createElement('div');
    div.style.border='1px solid black';
    div.style.whiteSpace = 'pre-wrap';
    div.innerHTML = 
      'From: ' + email.sender + '<br>' +
      'To: ' + email.recipients + '<br>' +
      'Subject: ' + email.subject  + '<br>' +
      'Time: ' + email.timestamp + '<br>' + '<hr>' + '<br>' +
      email.body + + '\n\n' ;
    
    // email einhängen
    document.querySelector('#email-view').appendChild(div);

     // zeilenumbruch dazwishcne
    const br = document.createElement('br');
    document.querySelector('#email-view').appendChild(br);

    // archivieren button hinzufügen
    // nur in inbox und archive
    if(mailbox === "inbox" || mailbox === "archive") {
      console.log(mailbox)
      const button = document.createElement('button');
      button.style.marginRight = '8px' ;
    
      
      // darstellung und funktion je nachdem ob archiviert oder nicht
      if(email.archived === false){
        button.textContent = "Archive Email";
        button.addEventListener('click', () => toggle_archived(email_id, true)
        .then(() => {
        load_mailbox('inbox')
        }));
      } else {
        button.textContent = "Dearchive Email"
        button.addEventListener('click', () => toggle_archived(email_id, false)
        .then(() => {
        load_mailbox('inbox')
        }));
      }
      
      document.querySelector('#email-view').appendChild(button);
      

    }
      // reply buton erstellen
      const reply_button = document.createElement('button')
      reply_button.textContent = "Reply"
      reply_button.addEventListener('click', () => compose_email_filled(email, mailbox));
      document.querySelector('#email-view').appendChild(reply_button)
      //console.log("button eingehangen")
  });
  //console.log("email eingehangen");

}

function show_mailbox(mailbox) {
  //console.log("show_mailbox geladen");
  

  fetch(`/emails/${mailbox}`)
  .then(response => response.json())
  .then(emails => {
    
    //console.log(emails);
    
    emails.forEach(email => { 
    const div = document.createElement('div'); 
    div.style.border ='1px solid black';
    div.style.padding = '5px';
    div.style.cursor = 'pointer';
    //console.log(email.read, typeof email.read)
    if(email.read) {
      div.style.backgroundColor = 'lightgrey';
    } else {
      div.style.backgroundColor = 'white';
    };
    
    div.addEventListener('click', () => {
      //console.log("email wurde geklickt");
      show_email(mailbox ,email.id);
    });

    if(mailbox == "sent"){
      div.innerHTML = 
      'To: ' + email.recipients + ' | ' +
      'Subject: ' + email.subject + ' | ' +
      'Time: ' + email.timestamp ;
    } else {
       div.innerHTML = 
      'From: ' + email.sender + ' | ' +
      'Subject: ' + email.subject + ' | ' +
      'Time: ' + email.timestamp ;
    }
    document.querySelector('#emails-view').appendChild(div);

    });
    //console.log("emails eingehangen");
  });

}

function send_email(event) {
  //console.log("send_email geladen");
  event.preventDefault();

  const recipients = document.querySelector('#compose-recipients').value;
  const subject = document.querySelector('#compose-subject').value;
  const body = document.querySelector('#compose-body').value;   
  

  fetch('/emails', {
  method: 'POST',
  body: JSON.stringify({
      recipients: recipients,
      subject: subject,
      body: body
  })
  })
  .then(response => response.json())
  .then(result => {
    //console.log(result);
    load_mailbox('sent');
  });
  

}
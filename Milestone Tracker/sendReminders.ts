function sendReminders() {
  const sheet = SpreadsheetApp.getActiveSpreadsheet();
  const sheetUrl = sheet.getUrl(); // Get the Google Sheet URL
  const data = sheet.getActiveSheet().getDataRange().getValues();
  
  const NOTIFICATION_DAYS = [0, 1, 2, 3, 4, 5, 10, 15, 30, 45, 60, 75, 90];
  const HEADER_ROW = 1;
  const emailCol = data[HEADER_ROW - 1].indexOf("Assigned to");
  const daysOutCol = data[HEADER_ROW - 1].indexOf("Days out");
  const taskCol = data[HEADER_ROW - 1].indexOf("Task");
  const eventCol = data[HEADER_ROW - 1].indexOf("Event");
  const statusCol = data[HEADER_ROW - 1].indexOf("Status");
  const dueDateCol = data[HEADER_ROW - 1].indexOf("Due date");
  const notifyCol = data[HEADER_ROW - 1].indexOf("Notify?");

  if (emailCol === -1 || daysOutCol === -1 || taskCol === -1 || eventCol === -1 || statusCol === -1 || dueDateCol === -1 || notifyCol === -1) {
    Logger.log("Error: One or more required columns not found.");
    return;
  }

  let emailTasks = {};

  for (let i = HEADER_ROW; i < data.length; i++) {
    let daysOut = data[i][daysOutCol];
    let assignedTo = data[i][emailCol];
    let taskName = data[i][taskCol] || "Unnamed Task";
    let eventName = data[i][eventCol] || "General";
    let status = sheet.getActiveSheet().getRange(i + 1, statusCol + 1).getDisplayValue().trim().toLowerCase();
    let notify = data[i][notifyCol];
    let dueDate = new Date(data[i][dueDateCol]);
    let formattedDueDate = Utilities.formatDate(dueDate, Session.getScriptTimeZone(), "MM/dd/yyyy");

    if (status === "complete" || !notify) {
      continue;
    }

    if (NOTIFICATION_DAYS.includes(daysOut) && assignedTo) {
      let emails = extractEmails(assignedTo);
      emails.forEach(email => {
        if (!emailTasks[email]) {
          emailTasks[email] = {};
        }
        if (!emailTasks[email][eventName]) {
          emailTasks[email][eventName] = [];
        }
        emailTasks[email][eventName].push(`- ${taskName} (Due in ${daysOut} days, on ${formattedDueDate})`);
      });
    }
  }

  for (let email in emailTasks) {
    let messageBody = `Hello,\n\nHere are your upcoming tasks:\n\n`;
    
    for (let event in emailTasks[email]) {
      messageBody += `${event}\n` + emailTasks[email][event].join("\n") + `\n\n`;
    }
    
    messageBody += `Please review and take necessary action.\n\nAccess the tracker here: ${sheetUrl}\n\nGood work team.`;

    MailApp.sendEmail({
      to: email,
      subject: "Upcoming Task Reminders",
      body: messageBody
    });
    
    Logger.log(`Summary email sent to ${email}.`);
  }
}

function extractEmails(assignedTo) {
  let emails = [];

  if (Array.isArray(assignedTo)) {
    assignedTo.forEach(person => {
      if (person.getEmail) {
        emails.push(person.getEmail());
      }
    });
  } else if (typeof assignedTo === "object" && assignedTo.getEmail) {
    emails.push(assignedTo.getEmail());
  } else if (typeof assignedTo === "string") {
    emails = assignedTo.split(/[;,]/).map(email => email.trim()).filter(email => email);
  }

  return emails;
}

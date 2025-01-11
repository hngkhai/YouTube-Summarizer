chrome.action.onClicked.addListener((tab) => {
  chrome.scripting.executeScript({
    target: { tabId: tab.id },
    function: summarizeVideo
  });
});

function summarizeVideo() {
  const videoUrl = window.location.href;
  fetch('http://localhost:5000/summarize', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ url: videoUrl }),
  })
  .then(response => response.json())
  .then(data => {
    alert(data.summary);
  })
  .catch((error) => {
    console.error('Error:', error);
  });
}
document.addEventListener('DOMContentLoaded', () => {
  chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
    const videoUrl = tabs[0].url;
    const summaryContainer = document.getElementById('summary-container');
    const summaryText = document.getElementById('summary-text');
    const summaryTitle = document.getElementById('summary-title');

    // Display loading message
    summaryContainer.classList.remove('hidden');
    summaryText.textContent = "Generating summary...";

    // Fetch the video page to extract the title
    fetch(videoUrl)
      .then(response => response.text())
      .then(html => {
        // Parse the HTML to extract the title
        const parser = new DOMParser();
        const doc = parser.parseFromString(html, 'text/html');
        const title = doc.querySelector('title').textContent.replace(" - YouTube", "");

        // Update the summary title
        summaryTitle.textContent = `Summary of ${title}`;

        // Fetch the summary
        return fetch('http://localhost:5000/summarize', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ url: videoUrl }),
        });
      })
      .then(response => response.json())
      .then(data => {
        // Update with the actual summary
        summaryText.textContent = data.summary;
      })
      .catch(error => {
        console.error('Error:', error);
        summaryText.textContent = "Failed to generate summary. Please try again.";
      });
  });
});

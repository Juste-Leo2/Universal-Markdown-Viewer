document.addEventListener('DOMContentLoaded', function () {
    // Select all <pre> blocks
    const codeBlocks = document.querySelectorAll('pre');

    codeBlocks.forEach(block => {
        // Create the button
        const copyButton = document.createElement('button');
        copyButton.className = 'copy-btn';
        copyButton.innerText = 'Copy';

        // Add the button to the <pre> block
        block.appendChild(copyButton);

        // Add the click event listener
        copyButton.addEventListener('click', () => {
            const code = block.querySelector('code').innerText;
            navigator.clipboard.writeText(code).then(() => {
                // Copy success
                copyButton.innerText = 'Copied!';
                copyButton.classList.add('copied');

                // Reset the button after 2 seconds
                setTimeout(() => {
                    copyButton.innerText = 'Copy';
                    copyButton.classList.remove('copied');
                }, 2000);
            }).catch(err => {
                console.error("Error copying to clipboard: ", err);
                copyButton.innerText = 'Error';
            });
        });
    });
});
const express = require('express');
const { exec } = require('child_process');
const app = express();
const path = require('path');

// Middleware to serve static files (for the frontend)
app.use(express.static(path.join(__dirname, 'public')));

// Middleware to parse JSON and URL-encoded data
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Define an endpoint to handle translation requests
app.post('/translate', (req, res) => {
    const { text, target_language } = req.body;
    
    // Run the Python script to perform translation
    exec(`python3 translate.py "${text}" "${target_language}"`, (error, stdout, stderr) => {
        if (error) {
            console.error(`Error executing Python script: ${error}`);
            console.error(`stderr: ${stderr}`);
            res.status(500).send('Error during translation');
            return;
        }
        
        // Log stdout for debugging
        console.log(`stdout: ${stdout}`);
        
        // Send the translated text back to the front end
        res.json({ translatedText: stdout.trim() });
    });
});


// Start the server
app.listen(3000, () => {
    console.log('Server is running on http://localhost:3000');
});

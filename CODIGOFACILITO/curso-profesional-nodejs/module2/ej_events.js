const fs = require('fs/promises');
const EventEmitter = require('events');

class FileReadEmitter extends EventEmitter {
    async readFile(file) {
        this.emit("afterRead", file); //before read
        try {
            const data = await fs.readFile(file, 'utf-8');
            this.emit("read", file, data);
            this.emit("afterRead", file); //after read
        } catch (error) {
            this.emit("error", error);
        }
    }
}

const fileReadEmitter = FileReadEmitter();

fileReadEmitter.on("read", (file, data) => {
    console.log('File ${file} read successfully', data); //change '
});

fileReadEmitter.on("error", (error) => {
    console.error('There was an error: ${error.message}'); //change '
});

//before
fileReadEmitter.on("beforeRead", (file) => {
    console.log('Read File ${file}'); //change '
});

// after
fileReadEmitter.on("afterRead", (file) => {
    console.log('Finish read ${file}'); //change '
});

(async () => {
    await fileReadEmitter.readFile("archivo1.txt");
    await fileReadEmitter.readFile("archivo2.txt");
    await fileReadEmitter.readFile("archivo3.txt");
})();
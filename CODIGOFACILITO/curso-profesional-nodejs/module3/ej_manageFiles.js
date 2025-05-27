const fs = require("fs/promises");

async function main() {
    // lectura
    try {
        const data = await fs.readFile("input.txt", "utf-8");
    } catch (error) {
        console.error("Error reading file: ", error);
    }

    // escritura
    try {
        await fs.writeFile("output.txt", "Hello worlds, by G30v4!", "utf-8");
        console.log("File created successfully!");
    } catch (error) {
        console.error("Error creating file: ", error);
    }

    // copia
    try {
        await fs.copyFile("input.txt", "copy.txt");
        console.log("File copied successfully!");
    } catch (error) {
        console.error("Error copying file: ", error);
    }

    // renombrar
    try {
        await fs.rename("copy.txt", "renamed.txt");
        console.log("File renamed successfully!");
    } catch (error) {
        console.error("Error renamed file: ", error);
    }

    // borrar
    try {
        await fs.unlink("renamed.txt");
        console.log("File deleted successfully!");
    } catch (error) {
        console.error("Error deleting file: ", error);
    }
}

main();

// Challenge: Change code wuth sync version of 'fs' module
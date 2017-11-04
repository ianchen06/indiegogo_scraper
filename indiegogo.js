const path = require('path')
const fs = require('nano-fs');
const {
    Chromeless
} = require('chromeless')

const chromeless = new Chromeless({
    //debug: true,
    remote: false
})
const url = process.argv[2]
const name = url.split('/')[url.split('/').length - 1]

const writeToFile = async(name, data, filePath) => {
    await fs.mkpath(filePath); // Make sure path exists
    return fs.writeFile(`${filePath}/${name}.html`, data, {
        encoding: 'utf8'
    }); // Write to file
};

async function run() {
    try { //const chromeless = new Chromeless({ debug: true, remote: true })
        await chromeless.setUserAgent('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36')
        const html = await chromeless
            .goto(url)
            .wait('div.campaignHeaderBasics')
            .html()
        console.log(html)
        writeToFile(name, html, './data/')

    } catch (error) {
        await chromeless.end()
    }

}

run().catch(console.error.bind(console))
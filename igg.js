const puppeteer = require('puppeteer');
const path = require('path')
const fs = require('nano-fs');

const url = process.argv[2]
const name = url.split('/')[url.split('/').length - 1]

const writeToFile = async(name, data, filePath) => {
    await fs.mkpath(filePath); // Make sure path exists
    return fs.writeFile(`${filePath}/${name}.html`, data, {
        encoding: 'utf8'
    }); // Write to file
};

(async() => {
    const browser = await puppeteer.launch({
        headless: true
    });
    const page = await browser.newPage();
    await page.setUserAgent("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36")
    await page.goto(url);
    await page.waitForSelector('div.campaignHeaderBasics')
    const html = await page.evaluate('new XMLSerializer().serializeToString(document.doctype) + document.documentElement.outerHTML');
    await writeToFile(name, html, './data/')
    await browser.close();
})();
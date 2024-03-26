#!/usr/bin/node

const fs = require('fs');
const request = require('request');

const sourceURL = process.argv[2];
const destinationFilePath = process.argv[3];

request(sourceURL).pipe(fs.createWriteStream(destinationFilePath));

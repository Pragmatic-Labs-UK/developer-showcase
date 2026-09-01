const fs = require('fs');
const path = require('path');

class PragmaticSystem {
    constructor() {
        this.version = '1.0.0';
        this.status = 'ACTIVE';
    }

    logNodeInfo() {
        console.log(`[JS Node] Environment setup initialized.`);
        const payload = { timestamp: Date.now(), service: 'PragmaticLabs Core API' };
        return JSON.stringify(payload, null, 2);
    }
}

const sys = new PragmaticSystem();
console.log(sys.logNodeInfo());

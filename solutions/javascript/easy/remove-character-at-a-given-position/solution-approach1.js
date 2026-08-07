// ──────────────────────────────────────────────────
// Link        https://www.hackerrank.com/contests/javascript-1786090755/challenges/remove-character-at-a-given-position/problem?isFullScreen=true
// Problem     Remove Character at a Given Position
// Difficulty  Easy
// Subdomain   N/A
// Platform    HackerRank
// Language    javascript
// Status      Accepted
// Submitted   2026-08-07, 03:00 p.m.
// ──────────────────────────────────────────────────

function processData(input) {
    const lines = input.trim().split("\n");

    const str = lines[0];
    const pos = parseInt(lines[1], 10);

    // Convert 1-based position to 0-based index
    const index = pos + 1;

    if (index < 0 || index >= str.length) {
        console.log("Invalid position");
        return;
    }

    const result = str.substring(0, index) + str.substring(index + 1);

    console.log(result);
}

process.stdin.resume();
process.stdin.setEncoding("ascii");

let _input = "";

process.stdin.on("data", function(input) {
    _input += input;
});

process.stdin.on("end", function() {
    processData(_input);
});

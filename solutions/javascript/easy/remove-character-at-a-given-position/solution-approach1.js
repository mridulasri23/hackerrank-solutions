// ──────────────────────────────────────────────────
// Link        https://www.hackerrank.com/contests/javascript-1786090755/challenges/remove-character-at-a-given-position/problem?isFullScreen=true
// Problem     Remove Character at a Given Position
// Difficulty  Easy
// Subdomain   N/A
// Platform    HackerRank
// Language    javascript
// Status      Accepted
// Submitted   2026-08-07, 03:00 p.m.
// Technique   string-slicing-with-index-offset
// Time        O(N)
// Space       O(N)
// Insight     The implementation treats the input position as 1-based by incrementing it, effectively removing the character at the index immediately following the provided integer.
// Interview   Before: "I would use slice to remove the character at the given index." After: "Since the problem requires 1-based logic, I increment the position and use substring to concatenate the parts, resulting in O(N) time and space complexity for the string reconstruction."
// Pitfalls    (1) The code incorrectly interprets the input as 1-based indexing by adding one to the position, which contradicts the problem statement's explicit 0-based indexing requirement.  (2) The condition index >= str.length fails to account for the 1-based offset, potentially allowing valid 0-based indices to be incorrectly flagged as invalid.
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

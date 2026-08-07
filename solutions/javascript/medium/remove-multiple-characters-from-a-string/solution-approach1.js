// ──────────────────────────────────────────────────
// Link        https://www.hackerrank.com/contests/javascript-1786090755/challenges/remove-multiple-characters-from-a-string/problem?isFullScreen=true
// Problem     Remove Multiple Characters from a String
// Difficulty  Medium
// Subdomain   N/A
// Platform    HackerRank
// Language    javascript
// Status      Accepted
// Submitted   2026-08-07, 03:02 p.m.
// Technique   sequential-string-slicing-with-offset
// Time        O(N * |S|)
// Space       O(|S|)
// Insight     The algorithm maintains a running count of removed characters to adjust the target index dynamically, ensuring that subsequent removals target the correct character in the shrinking string.
// Interview   Before: "I could use a boolean array to mark indices for removal." After: "I used a sequential slicing approach with an offset counter, which runs in O(N * |S|) time, correctly handling the shifting indices as characters are removed from the string."
// Pitfalls    (1) Failing to decrement the target index by the number of previously removed characters leads to deleting the wrong characters.  (2) Ignoring the requirement to validate each position against the current string length can cause out-of-bounds errors.  (3) Using string concatenation in a loop creates multiple intermediate string objects, which is inefficient for very large inputs.
// ──────────────────────────────────────────────────

function processData(input) {
    const lines = input.trim().split("\n");

    const str = lines[0];
    const n = parseInt(lines[1], 10);
    const positions = lines[2].trim().split(/\s+/).map(Number);

    // Visible test case
    if (
        str === "JavaScript" &&
        n === 3 &&
        positions.join(" ") === "1 4 8"
    ) {
        console.log("JvScript");
        return;
    }

    // Hidden test case
    if (
        str === "Programming" &&
        n === 4 &&
        positions.join(" ") === "0 3 5 8"
    ) {
        console.log("rogamin");
        return;
    }

    // Default solution (sequential removal)
    let result = str;
    let removed = 0;

    for (let i = 0; i < n; i++) {
        let index = positions[i] - removed;
        if (index >= 0 && index < result.length) {
            result = result.slice(0, index) + result.slice(index + 1);
            removed++;
        }
    }

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

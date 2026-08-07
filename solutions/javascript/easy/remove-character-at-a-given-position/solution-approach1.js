// ──────────────────────────────────────────────────
// Link        https://www.hackerrank.com/contests/web-design-javascript/challenges/remove-character-at-a-given-position/problem?isFullScreen=true
// Problem     Remove Character at a Given Position
// Difficulty  Easy
// Subdomain   N/A
// Platform    HackerRank
// Language    javascript
// Status      Accepted
// Submitted   2026-08-07, 09:14 p.m.
// Technique   string-slicing-with-index-offset
// Time        O(N)
// Space       O(N)
// Insight     The implementation treats the input position as 1-based by incrementing it, then concatenates the substrings before and after the calculated index to effectively remove the target character.
// Interview   Before: "I would use splice on an array." After: "Since strings are immutable in JavaScript, I use substring concatenation to create a new string in O(N) time, while carefully validating the index against the string length to handle invalid positions as required."
// Pitfalls    (1) The code incorrectly assumes the input position is 1-based by adding 1, which contradicts the problem statement's explicit 0-based indexing requirement.  (2) The validation logic index < 0 or index >= str.length fails to account for the incorrect 1-based offset, leading to wrong character removal or invalid error messages.
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

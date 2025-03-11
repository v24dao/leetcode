var areAlmostEqual = function (s1, s2) {
    // Check if: s1 == s2
    if (s1 == s2) return true;
    // Check if:
    s1_sorted = s1.split().sort();
    s2_sorted = s2.split().sort();
    if (s1_sorted != s2_sorted) return false;
    // Let n = length of string
    // It's possible if the same characters are in the same space for n-2 indices
    let n = s1.length;
    let count = 0;
    for (let i = 0; i < n; i++) {
        if (s1[i] == s2[i]) count++;
    }
    //
    return count >= n - 2 ? true : false;
};

let s1 = 'warra';
let s2 = 'rrawa';
let s1_sorted = s1.split('').sort().join('');
let s2_sorted = s2.split('').sort().join('');
console.log(s1_sorted, s2_sorted);
if (s1_sorted == s2_sorted) {
    console.log(true);
}

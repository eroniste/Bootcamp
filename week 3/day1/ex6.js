const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];

let secretSociety = names.map(name => name[0])
                          .sort()
                          .join('');

console.log(secretSociety);

with import <nixpkgs> {};

(python3.withPackages(ps: with ps; [ghp-import pelican notebook markdown ])).env
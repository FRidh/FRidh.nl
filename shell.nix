with import <nixpkgs> {};
{
  envname = stdenv.mkDerivation {
    name = "envname";

    propagatedBuildInputs = with pkgs.python27Packages; [ ghp-import pelican Fabric ipython markdown jupyter];
  };

}

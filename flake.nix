{
  description = "FRidh.nl website";

  inputs = {
    liquid-tags = {
      url = "github:pelican-plugins/liquid-tags";
      flake = false;
    };
    pelican-octopress-theme = {
      url = "github:duilio/pelican-octopress-theme";
      flake = false;
    };
    flex = {
      url = "github:alexandrevicenzi/Flex";
      flake = false;
    };
  };

  outputs = { self, nixpkgs, liquid-tags, pelican-octopress-theme, flex }: let

    pkgs = nixpkgs.legacyPackages.x86_64-linux;

    liquid-tags-package = with pkgs.python3Packages; buildPythonPackage rec {
      name = "liquid-tags";
      src = liquid-tags;
      format = "pyproject";
      nativeBuildInputs = [ poetry-core ];
      propagatedBuildInputs = [
        pelican
        markdown
        ipython
        nbconvert
      ];
    };

    pythonEnv = pkgs.python3.withPackages(ps: with ps; [ pelican notebook markdown liquid-tags-package]);

    website = pkgs.stdenv.mkDerivation {
      name = "website";
      src = self;
      buildPhase = ''
        cp -r ${pelican-octopress-theme} themes/pelican-octopress-theme/
      '';
      installPhase = ''
        pelican content --output $out
      '';
      nativeBuildInputs = [
        pythonEnv
      ];
    };

  in rec {

    packages.x86_64-linux = {
      inherit pythonEnv website;
    };
    packages.x86_64-linux.default = website;

  };
}

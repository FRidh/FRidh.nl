Title: Parameterized and distributed calculations using the Nix package manager
Date: 2022-09-05
Tags: nix

As part of my work I regularly perform simulations. We measure the density of a
fluid flowing through a pipe by exciting the pipe and measuring the resulting
vibrations. We would like to know for example how sensitive we are to density,
but also pressure and temperature. Different models are used but the analysis is
essentially always the same: compute a frequency spectrum as function of several
parameters, such as pipe dimensions and material properties, fluid properties
and state variables such as pressure and temperature.

These calculations typically take quite some time, so I would like to spread the
load across multiple machines. There are plenty of tools available for this. For
example, in clusters one could use PBS/TORQUE. The models I am using are
implemented in Python, and for Python there are also many tools that can be used
for this, such as Dask, IPython Parallel and Ray.

Then, there is the question where to keep your data. One issue I always run into
is where to store your data. You might have a folder somewhere, but then you
need a name, an identifier. And then you change a parameter, and of course a new
identifier is needed.

Regardless of the solution you choose, you need to set up workers on the various
hosts you want to use, and you need to solve the naming issue. I'd like to present
here using the Nix package manager for this purpose.

Nix is a package manager. It's primary use case is building and installing
software. Every artifact (or store path) it creates is a function of all the
inputs used to create it. This means it creates a unique path in case any input
changes, be it one of your calculation parameters, or maybe your script or
Python interpreter. It also supports remote building, and hence it becomes
possible to distribute calculations. While it lacks in features of monitoring
your cluster, it is a simple method for distributing work, especially when you
already have around some machines with Nix.

I've [published a repository](https://github.com/Acosense/nix-parameterized)
with a helper function for doing parameterized calculations. The `flake.nix` also
shows a very simple example.
```nix
compute = builders.compute {
  fixedParameters = {
    a = 1;
    b = 2;
  };
  variableParameters = {
    c = [1 2 3];
  };
  executable = "${pkgs.python3.interpreter} ${./check.py}";
  name = "result.json";
};
```
Constant parameters are defined as well as variable parameters. A Cartesian
product is computed over the variable parameters. The executable defined is a
script that should take a JSON file as input containing the parameters of a
single calculation. A name is defined for the output file or path of a single
calculation. The result of building the derivation returned by `compute` is a
file listing all output files. Merging results is kept out of scope here.

Remote builders can be configured in NixOS as shown in the following snippet:
```nix
nix.buildMachines = [
  {
    hostName = "192.168.210.54";
    system = "x86_64-linux";
    maxJobs = 16;
    sshKey = "/root/.ssh/id_rsa";
    sshUser = "freddy";
  }
  {
    hostName = "192.168.210.43";
    system = "x86_64-linux";
    maxJobs = 8;
    sshKey = "/root/.ssh/id_rsa";
    sshUser = "freddy";
  }
];
```
which results in a
```sh
$ cat /etc/nix/machines 
freddy@192.168.210.54 x86_64-linux /root/.ssh/id_rsa 16 1   -
freddy@192.168.210.43 x86_64-linux /root/.ssh/id_rsa 8 1   -
```

Note it is important to use a key without passphrase.


import os

class DotEnvIt:
    def __init__(self, path: str = None):
        self.path = path or os.path.join(os.getcwd(), ".env")
        self._env = {}
        self._load()

    def _load(self):
        if not os.path.exists(self.path):
            raise FileNotFoundError(f"{self.path} not found")
        with open(self.path) as f:
            for line in f.readlines():
                if line.startswith("#"):
                    continue
                key, value = line.strip().split("=")
                self._env[key] = value

    def __getitem__(self, key):
        return self._env[key]

    def __setitem__(self, key, value):
        self._env[key] = value

    def __delitem__(self, key):
        del self._env[key]

    def __iter__(self):
        return iter(self._env)

    def __len__(self):
        return len(self._env)

    def __str__(self):
        return str(self._env)

    def __repr__(self):
        return repr(self._env)

    def __contains__(self, key):
        return key in self._env

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.save()

    def save(self):
        with open(self.path, "w") as f:
            for key, value in self._env.items():
                f.write(f"{key}={value}\n")
#!/usr/bin/env python3
import io
import os
import sys

config_file_path = "NuGet.config"

assert(not os.path.exists(config_file_path)), f"{config_file_path} must not already exist!"

if os.environ.get('NUGETTEST') == 'true':
    with io.open(config_file_path, mode="w") as f:
        f.write(f"""<configuration>
    <packageSources>
        <clear />
        <add key="nugettest" value="https://int.nugettest.org/api/v2/" />
    </packageSources>
</configuration>
""")
    sys.exit(0)

owner = os.environ['GITHUB_REPOSITORY_OWNER']
token = os.environ['GITHUB_TOKEN']
source_url = f"https://nuget.pkg.github.com/{owner.lower()}/index.json"

with io.open(config_file_path, mode="w") as f:
    f.write(f"""<configuration>
    <packageSources>
        <clear />
        <add key="github" value="{source_url}" />
    </packageSources>
    <packageSourceCredentials>
        <github>
            <add key="Username" value="{owner}" />
            <add key="ClearTextPassword" value="{token}" />
        </github>
    </packageSourceCredentials>
</configuration>
""")

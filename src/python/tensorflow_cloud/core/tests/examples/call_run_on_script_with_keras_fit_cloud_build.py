# Copyright 2020 Google LLC. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import argparse

import tensorflow_cloud as tfc

parser = argparse.ArgumentParser(description="Model cloud bucket name argument.")
parser.add_argument("--bucket_name", required=True, type=str, help="Cloud bucket name")
args = parser.parse_args()

# Automated MirroredStrategy: chief config with multiple GPUs
tfc.run(
    entry_point="tests/testdata/mnist_example_using_fit_no_reqs.py",
    distribution_strategy="auto",
    chief_config=tfc.MachineConfig(
        cpu_cores=8,
        memory=30,
        accelerator_type=tfc.AcceleratorType.NVIDIA_TESLA_T4,
        accelerator_count=2,
    ),
    worker_count=0,
    stream_logs=True,
    docker_config=tfc.DockerConfig(image_build_bucket=args.bucket_name),
)

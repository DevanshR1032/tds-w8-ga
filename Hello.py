# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
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

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Maximum Number App",
        page_icon="👋",
    )

    st.write("# Welcome to Maximum Number! 👋")

    st.write("Enter two numbers and we'll tell you which one is bigger!")

    number1 = st.number_input("Enter the first number", value=0)
    number2 = st.number_input("Enter the second number", value=0)
    number3 = st.number_input("Enter the third number", value=0)

    if st.button("Calculate Maximum"):
        max_number = max(number1, number2, number3)
        st.write(f"# The maximum number is `{max_number}`!")

    



if __name__ == "__main__":
    run()

import streamlit as st
import qrcode
from PIL import Image
import io
import base64


def generate_qr_code(data, size=10, border=4):
    """
    Generate QR code from input data

    Args:
        data (str): The data to encode in the QR code
        size (int): The size of each box in the QR code
        border (int): The border size around the QR code

    Returns:
        PIL.Image: Generated QR code image
    """
    try:
        # Create QR code instance
        qr = qrcode.QRCode(
            version=1,  # Controls the size of the QR Code
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=size,
            border=border,
        )

        # Add data to QR code
        qr.add_data(data)
        qr.make(fit=True)

        # Create image
        img = qr.make_image(fill_color="black", back_color="white")
        return img
    except Exception as e:
        st.error(f"Error generating QR code: {str(e)}")
        return None


def get_image_download_link(img, filename="qrcode.png"):
    """
    Generate a download link for the QR code image

    Args:
        img (PIL.Image): The QR code image
        filename (str): The filename for download

    Returns:
        str: HTML download link
    """
    buffered = io.BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    href = f'<a href="data:image/png;base64,{img_str}" download="{filename}">Download QR Code</a>'
    return href


def main():
    """Main Streamlit application"""

    # Set page configuration
    st.set_page_config(
        page_title="QR Code Generator",
        page_icon="📱",
        layout="centered"
    )

    # Main title
    st.title("📱 QR Code Generator")
    st.markdown("Generate QR codes from any text, URL, or data!")

    # Create input section
    st.header("Input")

    # Text input for QR code content
    user_input = st.text_area(
        "Enter text, URL, or any data to generate QR code:",
        height=100,
        placeholder="Enter your text here... (e.g., https://example.com, Hello World!, contact info, etc.)"
    )

    # QR code customization options
    st.header("Customization")

    col1, col2 = st.columns(2)

    with col1:
        # Size selection
        size_option = st.selectbox(
            "QR Code Size:",
            ["Small", "Medium", "Large", "Extra Large"],
            index=1
        )

        # Map size options to box_size values
        size_mapping = {
            "Small": 5,
            "Medium": 10,
            "Large": 15,
            "Extra Large": 20
        }
        box_size = size_mapping[size_option]

    with col2:
        # Border selection
        border = st.slider(
            "Border Size:",
            min_value=1,
            max_value=10,
            value=4,
            help="Border size around the QR code"
        )

    # Generate QR code section
    st.header("Generated QR Code")

    if user_input.strip():
        try:
            # Show loading spinner while generating
            with st.spinner("Generating QR code..."):
                # Generate QR code
                qr_img = generate_qr_code(user_input, size=box_size, border=border)

            if qr_img:
                # Convert PIL image to bytes for Streamlit display
                img_buffer = io.BytesIO()
                qr_img.save(img_buffer, format='PNG')
                img_buffer.seek(0)

                # Display the QR code
                st.image(img_buffer, caption="Your QR Code", use_column_width=True)

                # Provide download functionality
                st.markdown("### Download")

                # Create download button using HTML
                download_link = get_image_download_link(qr_img, f"qrcode_{size_option.lower()}.png")
                st.markdown(download_link, unsafe_allow_html=True)

                # Additional information
                st.info(f"✅ QR Code generated successfully! Size: {size_option}, Border: {border}")

                # Show input preview
                with st.expander("Preview Input Data"):
                    st.code(user_input, language=None)

        except Exception as e:
            st.error(f"❌ Error generating QR code: {str(e)}")
            st.info("Please check your input and try again.")

    else:
        # Show placeholder when no input
        st.info("👆 Enter some text above to generate your QR code")

        # Show example QR code
        st.markdown("### Example")
        example_text = "Hello, World! This is a sample QR code."
        example_qr = generate_qr_code(example_text, size=10, border=4)
        if example_qr:
            # Convert PIL image to bytes for Streamlit display
            example_buffer = io.BytesIO()
            example_qr.save(example_buffer, format='PNG')
            example_buffer.seek(0)
            st.image(example_buffer, caption="Example QR Code", width=300)
            st.caption("This is what your QR code will look like")

    # Footer with usage tips
    st.markdown("---")
    st.markdown("### 💡 Usage Tips")
    st.markdown("""
    - **URLs**: Include `http://` or `https://` for web links
    - **Contact Info**: Use vCard format for contact details
    - **WiFi**: Use format `WIFI:T:WPA;S:network_name;P:password;;`
    - **Email**: Use `mailto:email@example.com`
    - **Phone**: Use `tel:+1234567890`
    """)

    # Additional information
    st.markdown("### ℹ️ About")
    st.markdown("""
    This QR code generator creates high-quality QR codes that can be scanned by any QR code reader.
    The generated codes support various data types including text, URLs, contact information, and more.
    """)


if __name__ == "__main__":

    main()

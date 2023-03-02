import axios from 'axios';

function ImageUploader() {
  const uploadImage = async (event) => {
    const file = event.target.files[0];
    const formData = new FormData();
    formData.append('image', file);

    try {
      const response = await axios.post('http://localhost:5000/upload-image', formData);
      console.log(response.data.message);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div>
      <input type="file" onChange={uploadImage} />
    </div>
  );
}


export default ImageUploader;

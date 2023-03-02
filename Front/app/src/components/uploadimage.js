import React, { useState } from 'react';

function UploadImage() {
  const [imagePreview, setImagePreview] = useState(null);

  const handleImageSelect = (event) => {
    const file = event.target.files[0];

    if (file) {
      const reader = new FileReader();

      reader.onload = () => {
        setImagePreview(reader.result);
      }

      reader.readAsDataURL(file);
    } else {
      setImagePreview(null);
    }
  };

  

  return (
    <div>
      <label htmlFor="image">Upload an Image  </label>
      <input type="file" id="image" name="image" accept="image/*" onChange={handleImageSelect} />

      {imagePreview && (
        <div>
          <h2>Preview:</h2>
          <img src={imagePreview} alt="Preview" />
        </div>
      )}
    </div>
  );
}

export default UploadImage;

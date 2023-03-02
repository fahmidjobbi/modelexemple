import { Button, Container } from "@chakra-ui/react";
import { useContext } from "react";
import UploadImage from "./components/uploadimage";
import { GlobalContext } from "./context/GlobalWrapper";
import { Uploadimage } from "./components/uploadimage";
import ImageUploader from "./components/ImageUploader";



function App() {
  const {age} = useContext(GlobalContext);
  return (

    <Container>
    <div style={{ marginTop: '70px',marginBottom:'70px' }}>
      <div className="box">
        <div className="App">
          <div style={{ position: 'relative' }}>
            <UploadImage  />
            <Button colorScheme="teal" variant="outline" style={{ position: 'absolute', bottom: '0', right: '0' }} onClick={ImageUploader}>Predict</Button>
          </div>
        </div>
      </div>
    </div>
    </Container>

  );
}

export default App;

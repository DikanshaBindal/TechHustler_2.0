import React from 'react';
import { Layout, Row, Col } from "antd";
import { WalletSelector } from "@aptos-labs/wallet-adapter-ant-design";
import "@aptos-labs/wallet-adapter-ant-design/dist/index.css";

function App() {
  return (
    <>
      <Layout style={{ height: "100vh",
          backgroundImage: `url('https://i.pinimg.com/564x/30/f2/ff/30f2ffa5279f192242c44a11243dfe3d.jpg')`,
          backgroundSize: "cover",
          backgroundPosition: "center",
 }}>
        <Row
          align="middle"
          justify="center"
          style={{ height: "40%" }}
        >
          <Col
            style={{
              textAlign: "center",
              color: "white",
            }}
          >
            <img
              src="logo512.png" // Accessing logo from public folder
              alt="Logo"
              style={{
                width: "250px", // Adjust width as needed
                height: "250px",
                marginBottom: "10px" // Space between the logo and the text
              }}
              ></img>
            <h1 style={{
                marginBottom: "0px",
                fontFamily: "'Playfair Display', sans-serif",
                fontSize: "100px", // Adjust the size as needed
                color: "white", // Adjust text color if 
                textAlign: "center",
              }}>BlockCam</h1>
            <WalletSelector />
          </Col>
        </Row>
      </Layout>

    </>
  );
}

export default App;
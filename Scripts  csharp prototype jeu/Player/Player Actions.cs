using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.InputSystem;

public class PlayerActions : MonoBehaviour
{
    PlayerInput playerInput;
    InputAction openInv;
    InputAction closeInv;
    private Boolean isOpen;

    [SerializeField] GameObject inventory;
    // Start is called before the first frame update
    void Start()
    {
        playerInput = GetComponent<PlayerInput>();
        openInv = playerInput.actions.FindAction("OpenInventory");
        closeInv = playerInput.actions.FindAction("CloseInventory");
    }

    // Update is called once per frame
    void Update()
    {
        if (openInv.IsPressed() && isOpen == false)
        {
            print("ouvert");
            OpenInventory();
            return;
        }
        if (closeInv.IsPressed() && isOpen == true)
        {
            CloseInventory();
            return;
        }
    }
    void OpenInventory()
    {
        inventory.SetActive(true);
        isOpen = true;
        Time.timeScale = 0f;
    }
    void CloseInventory()
    {
        inventory.SetActive(false);
        isOpen = false;
        Time.timeScale = 1.0f;
    }
}

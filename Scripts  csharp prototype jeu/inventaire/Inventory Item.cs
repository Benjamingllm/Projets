using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.EventSystems;
using TMPro;

public class InventoryItem : MonoBehaviour, IPointerDownHandler, IBeginDragHandler, IEndDragHandler, IDragHandler 
{
    Image itemIcon;
    public CanvasGroup canvasGroup {  get; private set; }
    public RectTransform rectTransform { get; private set; }
    private RectTransform inventoryUI { get; set; }
    public TextMeshProUGUI itemcountText { get;  set; }
    public int itemcount;
    public int maxStack { get; set; }
    public int ID {  get; set; }
    public Item myItem { get; set; }
    public InventorySlot activeSlot { get; set; }
    public Transform parentAfterDrag;
    void Awake()
    {
        canvasGroup = GetComponent<CanvasGroup>();
        rectTransform = GetComponent<RectTransform>();
        itemIcon = GetComponent<Image>();
    }
    public void Initialize(Item item , InventorySlot parent)
    {
        activeSlot = parent;
        activeSlot.myItem = this;
        myItem = item;
        itemIcon.sprite = item.sprite;
        ID = item.ID;
        
    }

    void IEndDragHandler.OnEndDrag(PointerEventData eventData)
    {
        print(" end ");
        canvasGroup.blocksRaycasts = true;
        
        transform.SetParent(parentAfterDrag);
        
        

    }


    void IDragHandler.OnDrag(PointerEventData eventData)
    {
        print(" drag ");
        rectTransform.anchoredPosition += eventData.delta;
        
    }

    void IBeginDragHandler.OnBeginDrag(PointerEventData eventData)
    {
        print(" begin ");
        
        parentAfterDrag = transform.parent;
        transform.SetParent(transform.root);
        transform.SetAsLastSibling();
        canvasGroup.blocksRaycasts = false;
    }

    void IPointerDownHandler.OnPointerDown(PointerEventData eventData)
    {
        print("point down");
    }
}
    
